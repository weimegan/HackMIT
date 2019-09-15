from rev_ai import apiclient
import time

accesscode = "022klht4it8TKsuK-Wh0YnLjGO1FHjAkHSw1kJoOGQ0xoFnGenH69BrgvJOS0J2bnr-iDqKL_Fyot_WfPuEyXS718p6p4"


def transcriber(recording_path):
    client = apiclient.RevAiAPIClient(accesscode)

    # you can send a local file
    job = client.submit_job_local_file(recording_path)

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
            list_of_jobs = client.get_list_of_jobs(
                limit=None, starting_after=None)

            # obtain transcript text as a string for the job.
            transcript_text = client.get_transcript_text(job.id)
            print(transcript_text)

            # Write to txt file
            f = open("transcript.txt", "w+")
            f.write(transcript_text)
            f.close()

            break
