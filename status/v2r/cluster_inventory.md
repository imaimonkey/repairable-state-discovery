# V2R cluster inventory

2026-09-25T09:35:06.438882+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837071872 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318837071872 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318837071872 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318837071872 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350374645760 available bytes; 98.39% used; 337556868 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22828220416 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22828220416 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22828220416 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22828220416 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331596656640 available bytes; 97.71% used; 445092506 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418932736 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418932736 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142301184000 available bytes; 98.03% used; 225810567 free inodes.

server3 `/tmp`: 84418932736 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418932736 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105623609344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105623609344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241722736640 available bytes; 96.66% used; 224994927 free inodes.

server4 `/tmp`: 105623609344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105623609344 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
