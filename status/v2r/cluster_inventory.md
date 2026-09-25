# V2R cluster inventory

2026-09-25T08:57:25.070799+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318838943744 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318838943744 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318838943744 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318838943744 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 364197318656 available bytes; 98.33% used; 337556995 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22830559232 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22830559232 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22830559232 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22830559232 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332660850688 available bytes; 97.70% used; 445093307 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84440219648 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84440219648 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142374232064 available bytes; 98.03% used; 225811202 free inodes.

server3 `/tmp`: 84440219648 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84440219648 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633169408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633169408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243392069632 available bytes; 96.64% used; 225000266 free inodes.

server4 `/tmp`: 105633169408 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633169408 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
