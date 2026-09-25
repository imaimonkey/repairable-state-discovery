# V2R cluster inventory

2026-09-25T04:32:58.522922+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318929743872 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318929743872 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318929743872 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318929743872 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 408724639744 available bytes; 98.13% used; 337591352 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22948954112 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22948954112 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22948954112 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22948954112 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462940770304 available bytes; 96.80% used; 445109872 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341239808 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84341239808 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143471185920 available bytes; 98.02% used; 225816086 free inodes.

server3 `/tmp`: 84341239808 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84341239808 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105671368704 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671368704 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32793710592 available bytes; 99.55% used; 224962821 free inodes.

server4 `/tmp`: 105671368704 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671368704 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
