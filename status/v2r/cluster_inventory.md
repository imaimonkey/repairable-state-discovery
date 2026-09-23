# V2R cluster inventory

2026-09-23T23:12:10.317291+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325671956480 available bytes; 81.83% used; 112501629 free inodes.

server1 `/home`: 325671956480 available bytes; 81.83% used; 112501629 free inodes.

server1 `/tmp`: 325671956480 available bytes; 81.83% used; 112501629 free inodes.

server1 `/var/tmp`: 325671956480 available bytes; 81.83% used; 112501629 free inodes.

server1 `/mnt/raid5`: 1387864510464 available bytes; 93.63% used; 337739748 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41059966976 available bytes; 97.71% used; 110432611 free inodes.

server2 `/home`: 41059966976 available bytes; 97.71% used; 110432611 free inodes.

server2 `/tmp`: 41059966976 available bytes; 97.71% used; 110432611 free inodes.

server2 `/var/tmp`: 41059966976 available bytes; 97.71% used; 110432611 free inodes.

server2 `/mnt/raid5`: 535042699264 available bytes; 96.30% used; 445206182 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292102127616 available bytes; 83.70% used; 114167341 free inodes.

server3 `/home`: 292102127616 available bytes; 83.70% used; 114167341 free inodes.

server3 `/data`: 82339442688 available bytes; 98.86% used; 225846375 free inodes.

server3 `/tmp`: 292102127616 available bytes; 83.70% used; 114167341 free inodes.

server3 `/var/tmp`: 292102127616 available bytes; 83.70% used; 114167341 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106269773824 available bytes; 94.07% used; 114353015 free inodes.

server4 `/home`: 106269773824 available bytes; 94.07% used; 114353015 free inodes.

server4 `/data`: 300039262208 available bytes; 95.85% used; 225429871 free inodes.

server4 `/tmp`: 106269773824 available bytes; 94.07% used; 114353015 free inodes.

server4 `/var/tmp`: 106269773824 available bytes; 94.07% used; 114353015 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
