import ru_local as ru

answer_1 = input(ru.SHORTHAIR)
match answer_1:
    case ru.YES:
        answer_2 = input(ru.CM_50)
        match answer_2:
            case ru.YES:
                answer_3 = input(ru.SHORT_TAIL)
                match answer_3:
                    case ru.YES:
                        print(ru.ENGLISH_BULLDOG)
                    case ru.NO:
                        answer_4 = input(ru.LONG_EARS)
                        match answer_4:
                            case ru.YES:
                                print(ru.SCENT_HOUND)
                            case ru.NO:
                                answer_5 = input(ru.SHORT_BODY)
                                match answer_5:
                                    case ru.YES:
                                        print(ru.PUG)
                                    case ru.NO:
                                        print(ru.CHIHUAHUA)
            case ru.NO:
                answer_3 = input(ru.KG_50)
                match answer_3:
                    case ru.YES:
                        print(ru.GREAT_DANE)
                    case ru.NO:
                        print(ru.FOXHOUND)
    case ru.NO:
        answer_2 = input(ru.CM_50)
        match answer_2:
            case ru.YES:
                answer_3 = input(ru.FRIENDLY)
                match answer_3:
                    case ru.YES:
                        print(ru.COCKER_SPANIEL)
                    case ru.NO:
                        print(ru.IRISH_SETTER)
            case ru.NO:
                answer_3 = input(ru.CM_70)
                match answer_3:
                    case ru.YES:
                        answer_4 = input(ru.LONG_EARS)
                        match answer_4:
                            case ru.YES:
                                print(ru.GRAND_GRIFFON_VENDEEN)
                            case ru.NO:
                                print(ru.COLLIE)
                    case ru.NO:
                        answer_4 = input(ru.ORANGE_WHITE)
                        match answer_4:
                            case ru.YES:
                                print(ru.SAINT_BERNARD)
                            case ru.NO:
                                answer_5 = input(ru.WHITE)
                                match answer_5:
                                    case ru.YES:
                                        print(ru.IRISH_WOLFHOUND)
                                    case ru.NO:
                                        print(ru.NEWFOUNDLAND)
