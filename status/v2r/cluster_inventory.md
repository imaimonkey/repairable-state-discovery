# V2R cluster inventory

2026-09-24T02:51:45.267315+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325384347648 available bytes; 81.85% used; 112498677 free inodes.

server1 `/home`: 325384347648 available bytes; 81.85% used; 112498677 free inodes.

server1 `/tmp`: 325384347648 available bytes; 81.85% used; 112498677 free inodes.

server1 `/var/tmp`: 325384347648 available bytes; 81.85% used; 112498677 free inodes.

server1 `/mnt/raid5`: 555150258176 available bytes; 97.45% used; 337732341 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40873603072 available bytes; 97.72% used; 110431384 free inodes.

server2 `/home`: 40873603072 available bytes; 97.72% used; 110431384 free inodes.

server2 `/tmp`: 40873603072 available bytes; 97.72% used; 110431384 free inodes.

server2 `/var/tmp`: 40873603072 available bytes; 97.72% used; 110431384 free inodes.

server2 `/mnt/raid5`: 528337027072 available bytes; 96.35% used; 445198707 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292285493248 available bytes; 83.69% used; 114186961 free inodes.

server3 `/home`: 292285493248 available bytes; 83.69% used; 114186961 free inodes.

server3 `/data`: 39727423488 available bytes; 99.45% used; 225845904 free inodes.

server3 `/tmp`: 292285493248 available bytes; 83.69% used; 114186961 free inodes.

server3 `/var/tmp`: 292285493248 available bytes; 83.69% used; 114186961 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002636800 available bytes; 94.08% used; 114349808 free inodes.

server4 `/home`: 106002636800 available bytes; 94.08% used; 114349808 free inodes.

server4 `/data`: 289728712704 available bytes; 96.00% used; 225386978 free inodes.

server4 `/tmp`: 106002636800 available bytes; 94.08% used; 114349808 free inodes.

server4 `/var/tmp`: 106002636800 available bytes; 94.08% used; 114349808 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
