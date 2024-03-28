// Get all sites names data

package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)



func GetSite(c *gin.Context) {

	// Define a slice to store the retrieved data
	var sites []Site

	// QUery db
	result := initializers.DB.Select("name").Find(&sites)
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of sites in the JSON response
	c.JSON(http.StatusOK, sites)
}