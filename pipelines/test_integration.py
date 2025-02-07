from tasks.build_database import execute as build_database


def test_build_database():
    """
    Test d'intégration pour la tâche build_database.

    On vérifie que la tâche build_database s'exécute correctement.
    Si une exception est levée, le test échoue, et le message d'erreur est affiché.
    Dans le cas contraire, le test est réussi.
    """
    try:
        build_database()
    except Exception as e:
        assert False, e
    assert True
