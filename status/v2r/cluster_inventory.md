# V2R cluster inventory

2026-09-25T09:18:11.258241+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837694464 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318837694464 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318837694464 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318837694464 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 350397116416 available bytes; 98.39% used; 337556934 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22836854784 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22836854784 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22836854784 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22836854784 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 332042588160 available bytes; 97.71% used; 445093175 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84434157568 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84434157568 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142374391808 available bytes; 98.03% used; 225810868 free inodes.

server3 `/tmp`: 84434157568 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84434157568 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632526336 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632526336 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241749475328 available bytes; 96.66% used; 224997136 free inodes.

server4 `/tmp`: 105632526336 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632526336 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
