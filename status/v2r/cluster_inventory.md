# V2R cluster inventory

2026-09-25T09:50:24.625827+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837915648 available bytes; 82.21% used; 112480388 free inodes.

server1 `/home`: 318837915648 available bytes; 82.21% used; 112480388 free inodes.

server1 `/tmp`: 318837915648 available bytes; 82.21% used; 112480388 free inodes.

server1 `/var/tmp`: 318837915648 available bytes; 82.21% used; 112480388 free inodes.

server1 `/mnt/raid5`: 350344495104 available bytes; 98.39% used; 337556788 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22834585600 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22834585600 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22834585600 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22834585600 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 331130372096 available bytes; 97.71% used; 445092019 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84416638976 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84416638976 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142296485888 available bytes; 98.03% used; 225810320 free inodes.

server3 `/tmp`: 84416638976 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84416638976 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614671872 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614671872 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240040210432 available bytes; 96.68% used; 224992960 free inodes.

server4 `/tmp`: 105614671872 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614671872 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
