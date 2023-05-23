from record_utils import *
from nlp_utils import *
from storage_utils import *


def main():
    path = "./audio.wav"
    start_recording_audio(path)
    transcript = get_transcript(path)
    transcript_processed = process_transcript(transcript)
    module_txt = generate_module(transcript_processed)
    keywords_txt = generate_keypoints(transcript_processed)
    text_to_pdf(transcript, "transcript.pdf")
    text_to_pdf(module_txt, "module.pdf")
    text_to_pdf(keywords_txt, "keypoints.pdf")


if __name__ == "__main__":
    main()

