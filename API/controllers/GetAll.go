// Get all route type and route count of all sites

package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

// Determine if NestedSite already exists for the current site. If it does, append the current route to the existing NestedSite,
// if it doesn't, create a new NestedSite for the current site.
func findSiteIndex(nestedRoutes []NestedSite, siteName string) int {
    for i, nestedRoute := range nestedRoutes {
        if nestedRoute.SiteName == siteName {
            return i // Return the index of the site if found
        }
    }
    return -1 // Return -1 if the site is not found
}


func GetAll(c *gin.Context) {

	// Define a slice to store the retrieved data
	var siteRouteContent []DbStructure

	// Query db
	result := initializers.DB.Table("site_route_content" ).Select("site_name", "route_type", "route_count").Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Define a slice to store the nested site data
	var allNestedRoutes []NestedSite
	// Iterate over the retrieved data to construct nested site structures
	for _, route := range siteRouteContent {
		nestedRoute := NestedRoute{
			RouteType: route.RouteType,
			RouteCount: route.RouteCount,
		}

		// Find the index of the site in the nested structure
		siteIndex := findSiteIndex(allNestedRoutes, route.SiteName)

		// Check if the site is already present in the nested structure
		if siteIndex == -1 {
			// If the site is not present, create a new nested site and append the route
			allNestedRoutes = append(allNestedRoutes, NestedSite{
				SiteName: route.SiteName,
				Routes: []NestedRoute{nestedRoute},
			})
		} else {
			// If the site is already present, append the route to its existing nested structure
			allNestedRoutes[siteIndex].Routes = append(allNestedRoutes[siteIndex].Routes, nestedRoute)
		}
	}

	// Return the list of sites names, routes and routes counts data in the JSON response
	c.JSON(http.StatusOK, allNestedRoutes)
}

