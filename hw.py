import boto3
import subprocess
import json

def deploy_hello_world_app(stack_name, template_file, region):
    try:
        # Initialize the AWS clients
        session = boto3.Session(region_name=region)
        client = session.client('cloudformation')

        # Package the SAM application
        package_command = f"sam package --template-file {template_file} --output-template-file packaged.yaml --s3-bucket seraj-s3-samcli"
        subprocess.run(package_command, shell=True, check=True)

        # Deploy the SAM application
        deploy_command = f"sam deploy --template-file packaged.yaml --stack-name {stack_name} --capabilities CAPABILITY_IAM --region {region}"
        subprocess.run(deploy_command, shell=True, check=True)

        print(f"Deployment of {stack_name} completed successfully.")

        # Get the API endpoint URL
        describe_stack_response = client.describe_stacks(StackName=stack_name)
        outputs = describe_stack_response['Stacks'][0].get('Outputs', [])
        api_endpoint = None
        for output in outputs:
            if output['OutputKey'] == 'HelloWorldApi':
                api_endpoint = output['OutputValue']
                break
        
        if api_endpoint:
            # Invoke the HelloWorld function
            invoke_command = f"curl {api_endpoint}/hello"
            result = subprocess.run(invoke_command, shell=True, capture_output=True, text=True)
            print(f"Invoked HelloWorld function. Response:\n{result.stdout}")
        else:
            print("Unable to find HelloWorldApi endpoint in stack outputs.")

    except subprocess.CalledProcessError as e:
        print(f"Error deploying {stack_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    stack_name = "HelloWorldStack"
    template_file = "template.yaml"
    region = "us-west-2"

    deploy_hello_world_app(stack_name, template_file, region)

