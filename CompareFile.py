import filecmp
filecmp.dircmp("/Source_folder", "/Destination_folder").report()

c = filecmp.dircmp("/Source_folder", "/Destination_folder",false)
report_recursive(c)

def report_recursive(dcmp):
    for name in dcmp.diff_files:
        print("DIFF file %s found in %s and %s" % (name, 
            dcmp.left, dcmp.right))
    for name in dcmp.left_only:
        print("ONLY LEFT file %s found in %s" % (name, dcmp.left))
    for name in dcmp.right_only:
        print("ONLY RIGHT file %s found in %s" % (name, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

