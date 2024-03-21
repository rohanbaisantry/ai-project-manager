export const AppConfig = {
  API_BASE_URL: ProcessingInstruction.env.VITE_API_BASE_URL ?? "https://localhost:8000",
  ENVIRONMENT: ProcessingInstruction.env.VIT_ENVIRONMENT_NAME ?? "LOCAL"
}
