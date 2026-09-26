# V2R cluster inventory

2026-09-26T06:11:43.342036+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318779166720 available bytes; 82.22% used; 112476277 free inodes.

server1 `/home`: 318779166720 available bytes; 82.22% used; 112476277 free inodes.

server1 `/tmp`: 318779166720 available bytes; 82.22% used; 112476277 free inodes.

server1 `/var/tmp`: 318779166720 available bytes; 82.22% used; 112476277 free inodes.

server1 `/mnt/raid5`: 221914251264 available bytes; 98.98% used; 337539896 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 20781477888 available bytes; 98.84% used; 110404637 free inodes.

server2 `/home`: 20781477888 available bytes; 98.84% used; 110404637 free inodes.

server2 `/tmp`: 20781477888 available bytes; 98.84% used; 110404637 free inodes.

server2 `/var/tmp`: 20781477888 available bytes; 98.84% used; 110404637 free inodes.

server2 `/mnt/raid5`: 273563090944 available bytes; 98.11% used; 445029312 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82430267392 available bytes; 95.40% used; 114110905 free inodes.

server3 `/home`: 82430267392 available bytes; 95.40% used; 114110905 free inodes.

server3 `/data`: 123993092096 available bytes; 98.29% used; 225822585 free inodes.

server3 `/tmp`: 82430267392 available bytes; 95.40% used; 114110905 free inodes.

server3 `/var/tmp`: 82430267392 available bytes; 95.40% used; 114110905 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105990254592 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105990254592 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 106912288768 available bytes; 98.52% used; 224929091 free inodes.

server4 `/tmp`: 105990254592 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105990254592 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
