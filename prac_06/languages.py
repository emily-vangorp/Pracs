from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

language_objects = [ruby, python, visual_basic]
programming_languages = []
for object in language_objects:
    programming_languages.append([object.name, object.is_dynamic, object.is_reflection, object.year])
print("The dynamically typed languages are:")
for language in programming_languages:
    if language[1] == "Dynamic":
        print(language[0])
    else:
        pass

