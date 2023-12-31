import glob
import os
from pathlib import Path
import shutil
import re
def run_scan_and_replace(raw_folder):
	raw_folder    = Path(raw_folder)
	cloned_folder = raw_folder.joinpath("Corrected") 
	if cloned_folder.exists():
		shutil.rmtree(cloned_folder)

	shutil.copytree(raw_folder, cloned_folder)
	
	paths_to_replace = ["//mal-nasuni/Legacy/Marks_CGI/LEGO/_PIPELINE",
						"/Volumes/legacy/Marks_CGI/LEGO/_PIPELINE",
						"B:/Marks_CGI/LEGO/_PIPELINE",
						"//dkafil-tma/Virtual_Solutions_WIP/_PIPELINE",
						"/Volumes/_PIPELINE"]

	path_to_replace_with = "//isln-smb/common/Lego/_PIPELINE"

	files_to_scan :list = list(cloned_folder.glob("**/layout*.ma")) + list(cloned_folder.glob("**/model.ma"))
	
	for file_path in files_to_scan:
		
		input_text = file_path.read_text()
		
		for path_to_find in paths_to_replace:
			
			input_text = re.sub(path_to_find, path_to_replace_with, input_text,flags=re.IGNORECASE)
			
		file_path.write_text(input_text)