/**
 * Dynamic API Base URL configuration.
 * Pulls from VITE_API_URL environment variable with a localhost fallback.
 */
export const API_BASE_URL = "";

/**
 * Helper to build API endpoints.
 * @param path The endpoint path (e.g., "/api/properties")
 */
export const getApiUrl = (path: string) => `${API_BASE_URL}${path.startsWith("/") ? "" : "/"}${path}`;
