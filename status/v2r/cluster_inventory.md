# V2R cluster inventory

2026-09-25T05:30:36.845567+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318875705344 available bytes; 82.21% used; 112480328 free inodes.

server1 `/home`: 318875705344 available bytes; 82.21% used; 112480328 free inodes.

server1 `/tmp`: 318875705344 available bytes; 82.21% used; 112480328 free inodes.

server1 `/var/tmp`: 318875705344 available bytes; 82.21% used; 112480328 free inodes.

server1 `/mnt/raid5`: 408494354432 available bytes; 98.13% used; 337568204 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22924107776 available bytes; 98.72% used; 110410508 free inodes.

server2 `/home`: 22924107776 available bytes; 98.72% used; 110410508 free inodes.

server2 `/tmp`: 22924107776 available bytes; 98.72% used; 110410508 free inodes.

server2 `/var/tmp`: 22924107776 available bytes; 98.72% used; 110410508 free inodes.

server2 `/mnt/raid5`: 440741896192 available bytes; 96.95% used; 445108060 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312883200 available bytes; 95.30% used; 114156041 free inodes.

server3 `/home`: 84312883200 available bytes; 95.30% used; 114156041 free inodes.

server3 `/data`: 142779252736 available bytes; 98.03% used; 225814797 free inodes.

server3 `/tmp`: 84312883200 available bytes; 95.30% used; 114156041 free inodes.

server3 `/var/tmp`: 84312883200 available bytes; 95.30% used; 114156041 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658400768 available bytes; 94.10% used; 114350397 free inodes.

server4 `/home`: 105658400768 available bytes; 94.10% used; 114350397 free inodes.

server4 `/data`: 26403282944 available bytes; 99.64% used; 224968224 free inodes.

server4 `/tmp`: 105658400768 available bytes; 94.10% used; 114350397 free inodes.

server4 `/var/tmp`: 105658400768 available bytes; 94.10% used; 114350397 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
