# V2R cluster inventory

2026-09-25T04:23:43.478867+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318930137088 available bytes; 82.21% used; 112480381 free inodes.

server1 `/home`: 318930137088 available bytes; 82.21% used; 112480381 free inodes.

server1 `/tmp`: 318930137088 available bytes; 82.21% used; 112480381 free inodes.

server1 `/var/tmp`: 318930137088 available bytes; 82.21% used; 112480381 free inodes.

server1 `/mnt/raid5`: 367461261312 available bytes; 98.31% used; 337592480 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22956204032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22956204032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22956204032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22956204032 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463241629696 available bytes; 96.80% used; 445110122 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340527104 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84340527104 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143689891840 available bytes; 98.01% used; 225816270 free inodes.

server3 `/tmp`: 84340527104 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84340527104 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105673801728 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105673801728 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 32807280640 available bytes; 99.55% used; 224963240 free inodes.

server4 `/tmp`: 105673801728 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105673801728 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
