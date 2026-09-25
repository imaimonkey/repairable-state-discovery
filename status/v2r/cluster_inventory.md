# V2R cluster inventory

2026-09-25T04:26:49.593072+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318929416192 available bytes; 82.21% used; 112480362 free inodes.

server1 `/home`: 318929416192 available bytes; 82.21% used; 112480362 free inodes.

server1 `/tmp`: 318929416192 available bytes; 82.21% used; 112480362 free inodes.

server1 `/var/tmp`: 318929416192 available bytes; 82.21% used; 112480362 free inodes.

server1 `/mnt/raid5`: 408745762816 available bytes; 98.12% used; 337592095 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22955237376 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22955237376 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22955237376 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22955237376 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463135961088 available bytes; 96.80% used; 445109901 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342431744 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84342431744 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143644581888 available bytes; 98.01% used; 225816208 free inodes.

server3 `/tmp`: 84342431744 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84342431744 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105671536640 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671536640 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32805089280 available bytes; 99.55% used; 224963110 free inodes.

server4 `/tmp`: 105671536640 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671536640 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
