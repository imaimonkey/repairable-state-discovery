# V2R cluster inventory

2026-09-25T01:06:48.616479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319077920768 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319077920768 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319077920768 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319077920768 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 416530616320 available bytes; 98.09% used; 337615677 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 23061069824 available bytes; 98.71% used; 110410768 free inodes.

server2 `/home`: 23061069824 available bytes; 98.71% used; 110410768 free inodes.

server2 `/tmp`: 23061069824 available bytes; 98.71% used; 110410768 free inodes.

server2 `/var/tmp`: 23061069824 available bytes; 98.71% used; 110410768 free inodes.

server2 `/mnt/raid5`: 498272841728 available bytes; 96.56% used; 445162221 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353449984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84353449984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148268490752 available bytes; 97.95% used; 225812755 free inodes.

server3 `/tmp`: 84353449984 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84353449984 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779580928 available bytes; 94.10% used; 114348301 free inodes.

server4 `/home`: 105779580928 available bytes; 94.10% used; 114348301 free inodes.

server4 `/data`: 53399441408 available bytes; 99.26% used; 225030870 free inodes.

server4 `/tmp`: 105779580928 available bytes; 94.10% used; 114348301 free inodes.

server4 `/var/tmp`: 105779580928 available bytes; 94.10% used; 114348301 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
