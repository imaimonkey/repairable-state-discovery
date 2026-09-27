# V2R cluster inventory

2026-09-27T11:22:40.390268+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304696659968 available bytes; 83.00% used; 112401642 free inodes.

server1 `/home`: 304696659968 available bytes; 83.00% used; 112401642 free inodes.

server1 `/tmp`: 304696659968 available bytes; 83.00% used; 112401642 free inodes.

server1 `/var/tmp`: 304696659968 available bytes; 83.00% used; 112401642 free inodes.

server1 `/mnt/raid5`: 634686316544 available bytes; 97.09% used; 337424397 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16433012736 available bytes; 99.08% used; 110353132 free inodes.

server2 `/home`: 16433012736 available bytes; 99.08% used; 110353132 free inodes.

server2 `/tmp`: 16433012736 available bytes; 99.08% used; 110353132 free inodes.

server2 `/var/tmp`: 16433012736 available bytes; 99.08% used; 110353132 free inodes.

server2 `/mnt/raid5`: 569875832832 available bytes; 96.06% used; 444737043 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78547652608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/home`: 78547652608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/data`: 1331996725248 available bytes; 81.59% used; 225759625 free inodes.

server3 `/tmp`: 78547652608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/var/tmp`: 78547652608 available bytes; 95.62% used; 114062817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030390784 available bytes; 93.80% used; 114372817 free inodes.

server4 `/home`: 111030390784 available bytes; 93.80% used; 114372817 free inodes.

server4 `/data`: 353613553664 available bytes; 95.11% used; 224728187 free inodes.

server4 `/tmp`: 111030390784 available bytes; 93.80% used; 114372817 free inodes.

server4 `/var/tmp`: 111030390784 available bytes; 93.80% used; 114372817 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
