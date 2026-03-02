// DealResponse.java
package com.deals.psychicdeals.dto;

import java.util.List;

public class DealResponse {

    public static class DealItem {
        private String skuId;
        private String name;
        private double price;
        private String storeId;
        private double score;
        // getters and setters
    }

    private String requestId;
    private List<DealItem> deals;
    private String reasoningSummary;

    // getters and setters
}
