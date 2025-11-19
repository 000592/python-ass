Guest=['Nopu','Maira','Davi']

print(f"Hello {Guest[0]}! I am inviting you for dinner at  6pm,I will be expecting you. ")

print(f"Hello {Guest[1]}! I am inviting you for dinner at  6pm,I will be expecting you. ")

print(f"Hello {Guest[2]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print("unfortunately {Guest[2]} cannot make it to dinner.")

Guest[2]='Raph'
print(f"Hello {Guest[0]}! I am inviting you for dinner at  6pm,I will be expecting you. ")

print(f"Hello {Guest[1]}! I am inviting you for dinner  at 6pm,I will be expecting you. ")

print(f"Hello {Guest[2]}! I am inviting you for dinner at  6pm,I will be expecting you. ")

print("Dear guest...I found a bigger dinning table,so more space will be available.")

Guest.insert(0,'Travis')

print(Guest)

Guest.insert(2,'Aquila')

print(Guest)

Guest.append('Leti')

print(Guest)

print(f"Hello {Guest[0]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print(f"Hello {Guest[1]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print(f"Hello {Guest[2]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print(f"Hello {Guest[3]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print(f"Hello {Guest[4]}! I am inviting you for dinner at 6pm,I will be expecting you. ")

print(f"Hello {Guest[5]}! I am inviting you for dinner at 6pm,I will be expecting you. ")


#starting with excercise seeing the world
print()
print()

Location=['Vatican City','Berlin','Zurich','New York']

print(Location)

print()

Location.sort()
print(Location)

Location.sort(reverse=True)
print(Location)

print()

Location.reverse()
print(Location)

Location.reverse()
print(Location)
print()

Location.sort()
print(Location)

Location.sort(reverse=True)
print(Location)