# V2R cluster inventory

2026-09-24T03:25:44.053621+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325356912640 available bytes; 81.85% used; 112498201 free inodes.

server1 `/home`: 325356912640 available bytes; 81.85% used; 112498201 free inodes.

server1 `/tmp`: 325356912640 available bytes; 81.85% used; 112498201 free inodes.

server1 `/var/tmp`: 325356912640 available bytes; 81.85% used; 112498201 free inodes.

server1 `/mnt/raid5`: 418087399424 available bytes; 98.08% used; 337733153 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40843067392 available bytes; 97.72% used; 110431134 free inodes.

server2 `/home`: 40843067392 available bytes; 97.72% used; 110431134 free inodes.

server2 `/tmp`: 40843067392 available bytes; 97.72% used; 110431134 free inodes.

server2 `/var/tmp`: 40843067392 available bytes; 97.72% used; 110431134 free inodes.

server2 `/mnt/raid5`: 527313600512 available bytes; 96.36% used; 445198328 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292379746304 available bytes; 83.68% used; 114201083 free inodes.

server3 `/home`: 292379746304 available bytes; 83.68% used; 114201083 free inodes.

server3 `/data`: 36722171904 available bytes; 99.49% used; 225843139 free inodes.

server3 `/tmp`: 292379746304 available bytes; 83.68% used; 114201083 free inodes.

server3 `/var/tmp`: 292379746304 available bytes; 83.68% used; 114201083 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987231744 available bytes; 94.09% used; 114349607 free inodes.

server4 `/home`: 105987231744 available bytes; 94.09% used; 114349607 free inodes.

server4 `/data`: 285156831232 available bytes; 96.06% used; 225385809 free inodes.

server4 `/tmp`: 105987231744 available bytes; 94.09% used; 114349607 free inodes.

server4 `/var/tmp`: 105987231744 available bytes; 94.09% used; 114349607 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
