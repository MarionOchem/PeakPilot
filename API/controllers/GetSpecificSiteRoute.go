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

	var siteRouteContent []NestedRoute
	result := initializers.DB.Table("site_route_content").Select("route_type", "route_count").Where("site_name = ? AND route_type = ?", site, route).Find(&siteRouteContent)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	response := Response{
		Site: site,
		Routes: siteRouteContent,
	}
	
	// Return the JSON response
	c.JSON(http.StatusOK, response)
}