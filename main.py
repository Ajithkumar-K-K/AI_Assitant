import extract_text
import recommendations
import ScreenClipTool
import notification

def main():
    Screenshot = ScreenClipTool.ScreenClipTool().cropped_image_path
    Text = str(extract_text.extract_text_from_file(Screenshot))
    Response = recommendations.get_recommendations(Text)
    notification.show_popup(Response)

if __name__ == "__main__":
    main()