from statistics import mean, median, mode
talliste = list(range(3,31,3))
talliste.append(77)
talliste.append(30)

print(talliste)
talliste.append(77)
print("max:", max(talliste))
print("min:" , min(talliste))
print("sum:" , sum(talliste))
print("mean:" , mean(talliste))
print("median:" , median(talliste))
print("mode:" , mode(talliste))
