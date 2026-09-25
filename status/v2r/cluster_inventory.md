# V2R cluster inventory

2026-09-25T03:22:06.967972+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318939721728 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318939721728 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318939721728 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318939721728 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 416104099840 available bytes; 98.09% used; 337599857 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22987608064 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22987608064 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22987608064 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22987608064 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 464610516992 available bytes; 96.79% used; 445112010 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84343586816 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84343586816 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 144657772544 available bytes; 98.00% used; 225810041 free inodes.

server3 `/tmp`: 84343586816 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84343586816 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692545024 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692545024 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45418713088 available bytes; 99.37% used; 224966843 free inodes.

server4 `/tmp`: 105692545024 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692545024 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
