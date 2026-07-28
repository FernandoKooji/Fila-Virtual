// ======================================
// Queue Mapper
// ======================================


// ======================================
// Lista da fila
// ======================================

export function mapQueue(response) {

    return response.queue ?? [];

}


// ======================================
// Status
// ======================================

export function mapQueueStatus(response) {

    return {

        currentTicket: response.current_ticket,

        priorityWaiting: response.priority_waiting,

        normalWaiting: response.normal_waiting,

        totalWaiting: response.total_waiting

    };

}