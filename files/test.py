from rev_ai import apiclient
import time


def transform (recording): 
    client = apiclient.RevAiAPIClient("022klht4it8TKsuK-Wh0YnLjGO1FHjAkHSw1kJoOGQ0xoFnGenH69BrgvJOS0J2bnr-iDqKL_Fyot_WfPuEyXS718p6p4")

    # recording = "C:/Users/Amanda/Downloads/test1.mp3"
    # you can send a local file
    job = client.submit_job_local_file(recording)

    # as text
    # transcript_text = client.get_transcript_text(job.id)

    while True:

    # Obtains details of a job in json format
        job_details = client.get_job_details(job.id)
        status = job_details.status.name

        print("Job Status : {}".format(status))

        # Checks if the job has been transcribed
        if status == "IN_PROGRESS":
            time.sleep(5)
            continue

        elif status == "FAILED":
            print("Job Failed : {}".format(job_details.failure_detail))
            break

        if status == "TRANSCRIBED":
            # Getting a list of current jobs connected with your account
            # The optional parameters limits limits the length of the list. Starting_after
            # Cuts off the beginning x jobs off the list returned
            list_of_jobs = client.get_list_of_jobs(limit=None, starting_after=None)

            # obtain transcript text as a string for the job.
            transcript_text = client.get_transcript_text(job.id)
            print(transcript_text)

            # obtain transcript text as a json object for the job.
            transcript_json = client.get_transcript_json(job.id)

            # obtain transcript object for the job.
            transcript_obj = client.get_transcript_object(job.id)

            # obtain captions for the job.
            captions = client.get_captions(job.id)

            break
# job_details = client.get_job_details(job.id)

# print(job_details.status)

