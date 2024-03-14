import PackageA
from PackageA import f1,f2
from PackageA.SubPackageA import f3,f4
from PackageA.SubPackageB import f5


# PackageA
print(f1.print_something())
print(f2.print_something())


# SubpackageA
print(f3.print_something())
print(f4.print_something())

# SubpackageB
print(f5.print_something())