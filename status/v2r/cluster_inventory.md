# V2R cluster inventory

2026-09-25T08:56:43.762585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318838964224 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318838964224 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318838964224 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318838964224 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 364198875136 available bytes; 98.33% used; 337556997 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22830682112 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22830682112 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22830682112 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22830682112 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332675518464 available bytes; 97.70% used; 445093231 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84440825856 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84440825856 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142374584320 available bytes; 98.03% used; 225811221 free inodes.

server3 `/tmp`: 84440825856 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84440825856 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105633181696 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633181696 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243393159168 available bytes; 96.64% used; 225000371 free inodes.

server4 `/tmp`: 105633181696 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633181696 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
