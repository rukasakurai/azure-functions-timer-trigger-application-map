# Azure Functions Timer Trigger with Application Map

This project demonstrates a timer-triggered Azure Function that calls an HTTP-triggered Function, with distributed tracing to visualize the dependencies in Application Insights Application Map.

## Project Structure

- `infra/`: Contains Bicep infrastructure as code
  - `main.bicep`: Defines all Azure resources (Function App, Storage, App Insights)
- `src/app/`: Contains the Function App code
  - `TimerFunction/`: A timer-triggered function that calls the HTTP function
  - `HttpFunction/`: An HTTP-triggered function that returns a simple response

## Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Developer CLI (azd)](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)
- [Python](https://www.python.org/downloads/) 3.8 or later
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools) version 4.x

## Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/rukasakurai/azure-functions-timer-trigger-application-map.git
   cd azure-functions-timer-trigger-application-map
   ```

2. Install dependencies:

   ```bash
   cd src/app
   pip install -r requirements.txt
   ```

3. Run the Functions locally:
   ```bash
   func start
   ```

## Deployment using Azure Developer CLI (azd)

The Azure Developer CLI (azd) provides a consistent way to provision infrastructure and deploy code for your application.

### Deploy the application

1. Login to Azure:

   ```bash
   azd auth login
   ```

2. Initialize your environment:

   ```bash
   azd init
   ```

   - If asked about the project structure, select that it's already set up for azd.

3. Provision the infrastructure and deploy the code:

   ```bash
   azd up
   ```

   - This command will:
     - Create an Azure resource group (or use the specified one)
     - Provision all resources defined in the Bicep template
     - Build and deploy the Function App code
     - Configure application settings

4. When prompted, select or create an environment name and select your subscription.

### View the deployment results

After a successful deployment, you'll see output with URLs and other important information:

- Function App URL
- Application Insights URL

### Monitor the application

1. Navigate to the deployed Function App in the Azure Portal
2. Go to the "Application Insights" section
3. Click on "Application Map" to visualize the dependencies between the Timer Function and HTTP Function

## Clean Up Resources

To delete all created resources when you're done:

```bash
azd down
```
