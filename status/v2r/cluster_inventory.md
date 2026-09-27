# V2R cluster inventory

2026-09-27T09:25:19.999280+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314452467712 available bytes; 82.46% used; 112440738 free inodes.

server1 `/home`: 314452467712 available bytes; 82.46% used; 112440738 free inodes.

server1 `/tmp`: 314452467712 available bytes; 82.46% used; 112440738 free inodes.

server1 `/var/tmp`: 314452467712 available bytes; 82.46% used; 112440738 free inodes.

server1 `/mnt/raid5`: 635457544192 available bytes; 97.08% used; 337424515 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16515833856 available bytes; 99.08% used; 110356952 free inodes.

server2 `/home`: 16515833856 available bytes; 99.08% used; 110356952 free inodes.

server2 `/tmp`: 16515833856 available bytes; 99.08% used; 110356952 free inodes.

server2 `/var/tmp`: 16515833856 available bytes; 99.08% used; 110356952 free inodes.

server2 `/mnt/raid5`: 573787426816 available bytes; 96.04% used; 444742078 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78556028928 available bytes; 95.62% used; 114062914 free inodes.

server3 `/home`: 78556028928 available bytes; 95.62% used; 114062914 free inodes.

server3 `/data`: 1332499075072 available bytes; 81.58% used; 225762468 free inodes.

server3 `/tmp`: 78556028928 available bytes; 95.62% used; 114062914 free inodes.

server3 `/var/tmp`: 78556028928 available bytes; 95.62% used; 114062914 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050506240 available bytes; 93.80% used; 114372845 free inodes.

server4 `/home`: 111050506240 available bytes; 93.80% used; 114372845 free inodes.

server4 `/data`: 364102184960 available bytes; 94.97% used; 224767404 free inodes.

server4 `/tmp`: 111050506240 available bytes; 93.80% used; 114372845 free inodes.

server4 `/var/tmp`: 111050506240 available bytes; 93.80% used; 114372845 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
