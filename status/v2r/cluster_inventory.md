# V2R cluster inventory

2026-09-24T03:01:55.794408+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325372882944 available bytes; 81.85% used; 112498522 free inodes.

server1 `/home`: 325372882944 available bytes; 81.85% used; 112498522 free inodes.

server1 `/tmp`: 325372882944 available bytes; 81.85% used; 112498522 free inodes.

server1 `/var/tmp`: 325372882944 available bytes; 81.85% used; 112498522 free inodes.

server1 `/mnt/raid5`: 511707291648 available bytes; 97.65% used; 337732294 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40861564928 available bytes; 97.72% used; 110431310 free inodes.

server2 `/home`: 40861564928 available bytes; 97.72% used; 110431310 free inodes.

server2 `/tmp`: 40861564928 available bytes; 97.72% used; 110431310 free inodes.

server2 `/var/tmp`: 40861564928 available bytes; 97.72% used; 110431310 free inodes.

server2 `/mnt/raid5`: 528031129600 available bytes; 96.35% used; 445198666 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292289363968 available bytes; 83.69% used; 114187109 free inodes.

server3 `/home`: 292289363968 available bytes; 83.69% used; 114187109 free inodes.

server3 `/data`: 39701635072 available bytes; 99.45% used; 225845323 free inodes.

server3 `/tmp`: 292289363968 available bytes; 83.69% used; 114187109 free inodes.

server3 `/var/tmp`: 292289363968 available bytes; 83.69% used; 114187109 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105988345856 available bytes; 94.09% used; 114349629 free inodes.

server4 `/home`: 105988345856 available bytes; 94.09% used; 114349629 free inodes.

server4 `/data`: 289714024448 available bytes; 96.00% used; 225386865 free inodes.

server4 `/tmp`: 105988345856 available bytes; 94.09% used; 114349629 free inodes.

server4 `/var/tmp`: 105988345856 available bytes; 94.09% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
