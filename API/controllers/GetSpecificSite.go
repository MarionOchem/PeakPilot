// Get all routes types and count from a specific site

package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetSpecificSite(c *gin.Context) {
	// Retrieve site parameter from the HTTP request 
	site := c.Param("site")

	// Define a slice to store the retrieved data
	var siteRouteContent []DbStructure

	// Query db
	result := initializers.DB.Table("site_route_content").Select("site_name", "route_type", "route_count").Where("site_name = ?", site).Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Define a slice to store the nested routes data 
	var nestedRoutes []NestedRoute
	// Iterate over the retrieved data to construct nested site structure
	for _, route := range siteRouteContent {
		// Create a nested route object
		nestedRoute := NestedRoute{
			RouteType:  route.RouteType,
			RouteCount: route.RouteCount,
		}
		// Append the route to the nested site structure
		nestedRoutes = append(nestedRoutes, nestedRoute)
	}

	nestedSite := NestedSite{
		SiteName: site,
		Routes: nestedRoutes,
	}

	// Return the routes data for the specific site in the JSON response
	c.JSON(http.StatusOK, nestedSite)
}