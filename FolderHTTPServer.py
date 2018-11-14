import os
from http.server import BaseHTTPServer
import json

class FolderHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		fullpath=self.path.split('?')
		path=fullpath[0]
		cwd=os.getcwd()+path
		if len(fullpath) == 1:
			query = ''
		else:
			query = fullpath[1]
			fullquery=query.split('-')
			query_argument =fullquery[0]
			query_parameter=fullquery[1]
			if query_argument =='createfolder':
				os.mkdir(cwd+'/'+query_parameter)
			if query_argument == 'deletefolder':
				os.rmdir(cwd+'/'+query_parameter,dir_fd=None)
		folder_tree = []
		self.send_response(200)
		if os.path.isfile(cwd):
			self.send_header('content-dispsition','attachment')
		else:
			self.send_header('content-type','application/json')
			for listitem in os.listdir(cwd):
				listitem_path = os.path.join(cwd,listitem)
				json_string = {'Name':os.path.basename(listitem_path),'Path':'/'+os.path.basename(listitem_path),'Type':Type}
				if os.path.isfile(listitem_path):
					json_string.update(Type='file')
				else:
					json_string.update(Type='folder')
				folder_tree.append(json_string)
		self.end_haeders()
		jsonobject=json.dumps(folder_tree)
		self.wfile.write(jsonobject.encode())