# V2R cluster inventory

2026-09-23T16:10:56.752010+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41412509696 available bytes; 97.69% used; 110435189 free inodes.

server2 `/home`: 41412509696 available bytes; 97.69% used; 110435189 free inodes.

server2 `/tmp`: 41412509696 available bytes; 97.69% used; 110435189 free inodes.

server2 `/var/tmp`: 41412509696 available bytes; 97.69% used; 110435189 free inodes.

server2 `/mnt/raid5`: 549367029760 available bytes; 96.20% used; 445218212 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 317829046272 available bytes; 82.26% used; 114295927 free inodes.

server3 `/home`: 317829046272 available bytes; 82.26% used; 114295927 free inodes.

server3 `/data`: 119459368960 available bytes; 98.35% used; 225854443 free inodes.

server3 `/tmp`: 317829046272 available bytes; 82.26% used; 114295927 free inodes.

server3 `/var/tmp`: 317829046272 available bytes; 82.26% used; 114295927 free inodes.
| server4 | True | ['1', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498928128 available bytes; 93.78% used; 114375788 free inodes.

server4 `/home`: 111498928128 available bytes; 93.78% used; 114375788 free inodes.

server4 `/data`: 37430353920 available bytes; 99.48% used; 225486562 free inodes.

server4 `/tmp`: 111498928128 available bytes; 93.78% used; 114375788 free inodes.

server4 `/var/tmp`: 111498928128 available bytes; 93.78% used; 114375788 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
