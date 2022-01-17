import speech_recognition as s_r
import window

all_available_microphones = []
picture_for_camera_view = ""

def main():
    # update_available_microphones()
    print(all_available_microphones)
    window.create_window()
    return

# def update_available_microphones():
#     all_available_microphones.clear()

#     for name in s_r.Microphone.list_microphone_names():
#         all_available_microphones.append(name)

if __name__ == "__main__":
    main()