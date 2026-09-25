# V2R cluster inventory

2026-09-25T11:19:17.385849+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319061876736 available bytes; 82.20% used; 112478863 free inodes.

server1 `/home`: 319061876736 available bytes; 82.20% used; 112478863 free inodes.

server1 `/tmp`: 319061876736 available bytes; 82.20% used; 112478863 free inodes.

server1 `/var/tmp`: 319061876736 available bytes; 82.20% used; 112478863 free inodes.

server1 `/mnt/raid5`: 364169830400 available bytes; 98.33% used; 337550313 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] |

server2 `/`: 22905688064 available bytes; 98.72% used; 110409986 free inodes.

server2 `/home`: 22905688064 available bytes; 98.72% used; 110409986 free inodes.

server2 `/tmp`: 22905688064 available bytes; 98.72% used; 110409986 free inodes.

server2 `/var/tmp`: 22905688064 available bytes; 98.72% used; 110409986 free inodes.

server2 `/mnt/raid5`: 327875915776 available bytes; 97.73% used; 445084078 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84141273088 available bytes; 95.30% used; 114155498 free inodes.

server3 `/home`: 84141273088 available bytes; 95.30% used; 114155498 free inodes.

server3 `/data`: 142087704576 available bytes; 98.04% used; 225814374 free inodes.

server3 `/tmp`: 84141273088 available bytes; 95.30% used; 114155498 free inodes.

server3 `/var/tmp`: 84141273088 available bytes; 95.30% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105611911168 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611911168 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238631784448 available bytes; 96.70% used; 224981374 free inodes.

server4 `/tmp`: 105611911168 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611911168 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
