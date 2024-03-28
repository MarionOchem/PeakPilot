// Get a specific route type and count from a specific site

package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetSpecificSiteRoute(c *gin.Context) {
	// Retrieve site parameter from the HTTP request 
	site := c.Param("site")
	route := c.Param("route")

	// Define a slice to store the retrieved data
	var siteRouteContent []NestedRoute

	// Query db
	result := initializers.DB.Table("site_route_content").Select("route_type", "route_count").Where("site_name = ? AND route_type = ?", site, route).Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Create a response object 
	response := Response{
		Site: site,
		Routes: siteRouteContent,
	}
	
	// Return the JSON response
	c.JSON(http.StatusOK, response)
}