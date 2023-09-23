def elements_in_union(intersection_abc, intersection_ab, intersection_ac, intersection_bc, set_a, set_b, set_c):
    union_abc = intersection_abc + intersection_ab + intersection_ac + intersection_bc + set_a + set_b + set_c
    return union_abc

intersection_abc = 3
intersection_ab = 2
intersection_ac = 2
intersection_bc = 2
set_a = 5
set_b = 4
set_c = 6
union_elements = elements_in_union(intersection_abc, intersection_ab, intersection_ac, intersection_bc, set_a, set_b, set_c)
print(f"Number of elements in union: {union_elements}")
