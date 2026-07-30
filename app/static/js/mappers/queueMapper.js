// ======================================
// Queue Mapper
// ======================================

export function mapQueue(response) {

    if (Array.isArray(response)) {

        return response;

    }

    return response.queue ?? [];

}

export function mapQueueStatus(response) {

    return {

        currentTicket: response.current_ticket,

        priorityWaiting: response.priority_waiting,

        normalWaiting: response.normal_waiting,

        totalWaiting: response.total_waiting

    };

}