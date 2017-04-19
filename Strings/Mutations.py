def mutate_string(string, position, character):
    
    return string[:position] + character + string[position+1:]

string = raw_input()
position, character = raw_input().split()

print mutate_string(string, int(position), character)