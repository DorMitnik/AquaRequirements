from requirements_parser import RequirementsParser


def main():
    requirements_parser = RequirementsParser()
    path = "one_requirement.txt"
    requirements_parser.create_final_requirements_file(path)


if __name__ == '__main__':
    main()
