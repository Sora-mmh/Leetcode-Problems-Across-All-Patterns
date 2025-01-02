class Solution:
    def simplifyPath(self, path: str) -> str:
        files = []
        split = path.split("/")
        for e in split:
            if files and e == "..":
                files.pop()
            elif e not in [".", "", ".."]:
                files.append(e)
        return "/" + "/".join(files)
        
