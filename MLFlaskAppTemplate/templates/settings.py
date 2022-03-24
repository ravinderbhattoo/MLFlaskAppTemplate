def generate_settings(app_name):
    return """{
    "APP_NAME": """ + f'"{app_name}"' + """,
    "MY_MODELS": {
        "Model Name": {
            "file": "model.pkl", 
            "test_X": "test_X.csv", 
            "test_y": "test_y.csv", 
            "mean_std": "mean_std.json"
            },
        "Model Name 2": {
            "file": "model.pkl", 
            "test_X": "test_X.csv", 
            "test_y": "test_y.csv", 
            "mean_std": "mean_std.json"
            }
    }
}
"""