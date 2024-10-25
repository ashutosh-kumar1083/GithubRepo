import pkg_resources

def is_package_installed(package_name):
	try:
		pkg_resources.get_distribution(package_name)
		return True
	except pkg_resources.DistributionNotFound:
		return False

# Example usage for checking if 'numpy' is installed
pkgName = input("Search for package:")
if is_package_installed(pkgName):
	print(pkgName + " is installed")
else:
	print(pkgName + " is not installed")

