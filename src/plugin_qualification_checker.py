import os
import json
import threading
import zlib
import struct
import shutil

class qualification_checker():
    def scan(path: str) -> dict:
        qualification_checker.lock = threading.Lock()
        all_plugins: list[str] = qualification_checker.get_from_file("ESLifier_Data/plugin_list.json")
        qualification_checker.maxed_masters = qualification_checker.get_from_file("ESLifier_Data/maxed_masters.json")
        plugin_blacklist = ("Skyrim.esm", "Update.esm", "HearthFires.esm", "Dragonborn.esm", "Dawnguard.esm")
        plugins = [plugin for plugin in all_plugins if not plugin.lower().endswith('.esl') and os.path.basename(plugin) not in plugin_blacklist]
        qualification_checker.missing_skyrim_esm_as_master: dict[str, str] = qualification_checker.get_from_file("ESLifier_Data/missing_skyrim_as_master.json")
        qualification_checker.dependent_dict: dict[str, list[str]] = qualification_checker.get_from_file("ESLifier_Data/dependency_dictionary.json")
        qualification_checker.flag_dict = {}
        qualification_checker.max_record_number = 4096
        if os.path.exists('ESLifier_Data/EDIDs'):
            shutil.rmtree('ESLifier_Data/EDIDs')
        if not os.path.exists("ESLifier_Data/EDIDs"):
            os.makedirs("ESLifier_Data/EDIDs")

        if len(plugins) > 1000:
            split = 5
        elif len(plugins) > 500:
            split = 2
        else:
            split = 1

        chunk_size = len(plugins) // split
        chunks = [plugins[i * chunk_size:(i + 1) * chunk_size] for i in range(split)]
        chunks.append(plugins[(split) * chunk_size:])

        threads: list[threading.Thread] = []
        for chunk in chunks:
            thread = threading.Thread(target=qualification_checker.plugin_scanner, args=(chunk,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
        with open('ESLifier_Data/flag_dictionary.json', 'w', encoding='utf-8') as f:
            json.dump(qualification_checker.flag_dict, f, ensure_ascii=False, indent=4)
        return qualification_checker.flag_dict

    def plugin_scanner(plugins: list):
        flag_dict: dict[str, list[str]] = {}
        for i, plugin in enumerate(plugins):
            print(f'\033[F\033[K-  Reading plugin {i} of {len(plugins)} plugins ({os.path.basename(plugin)})\n-', end='\r')
            is_esm = qualification_checker.is_file_esm(plugin)
            esl_allowed, need_compacting, new_wrld, new_wthr, record_count = qualification_checker.file_reader(plugin)
            if esl_allowed:
                flag_dict[plugin] = []
                if need_compacting:
                    flag_dict[plugin].append('need_compacting')
                if new_wrld:
                    flag_dict[plugin].append('new_wrld')
                if new_wthr:
                    flag_dict[plugin].append('new_wthr')
                if is_esm:
                    flag_dict[plugin].append('is_esm')

            flag_dict[plugin].append({'record_count': record_count})

        print(f'\033[F\033[K-  Read {len(plugins)} plugins\n', end='\r')
                        
        with qualification_checker.lock:
            for key, value in flag_dict.items():
                if key not in qualification_checker.flag_dict:
                    qualification_checker.flag_dict[key] = value

    def create_data_list(data: bytes) -> list:
        data_list = []
        offset = 0
        while offset < len(data):
            if data[offset:offset+4] == b'GRUP':
                data_list.append(data[offset:offset+24])
                offset += 24
            else:
                form_length = struct.unpack("<I", data[offset+4:offset+8])[0]
                offset_end = offset + 24 + form_length
                data_list.append(data[offset:offset_end])
                offset = offset_end
        return data_list      

    def file_reader(file: str) -> tuple[bool, bool, bool, bool, bool]:
        data_list = []
        try:
            with open(file, 'rb') as f:
                data = f.read()
            data_list = qualification_checker.create_data_list(data)
        except Exception as e:
            print(f'!Error: Failed to read plugin: {file}')
            print(e) 
            return False, False, False, False, False, False

        master_count = qualification_checker.get_master_count(data_list)

        count = 0
        need_compacting = False
        new_wrld = False
        new_wthr = False
        for form in data_list:
            record_type = form[:4]
            if record_type not in (b'GRUP', b'TES4') and form[15] >= master_count:
                count += 1
                if record_type == b'WRLD':
                    new_wrld = True

                if record_type == b'WTHR':
                    new_wthr = True
        
        return True, need_compacting, new_wrld, new_wthr, count

    def is_file_esm(file: str) -> bool:
        with open(file, 'rb') as f:
            if file.lower().endswith('.esm'):
                return True
            f.seek(8)
            esm_flag = f.read(1)
            if esm_flag in (b'\x81', b'\x01'):
                return True
            return False
            
    def get_from_file(file: str) -> list | dict:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = []
        return data
    
    def get_master_count(data_list: list) -> tuple[int, bool]:
        tes4 = data_list[0]
        offset = 24
        data_len = len(tes4)
        master_count = 0
        while offset < data_len:
            field = tes4[offset:offset+4]
            field_size = struct.unpack("<H", tes4[offset+4:offset+6])[0]
            if field == b'MAST':
                master_count += 1
            offset += field_size + 6

        return master_count